/**
  * Bespin: reference implementations of "big data" algorithms
  *
  * Licensed under the Apache License, Version 2.0 (the "License");
  * you may not use this file except in compliance with the License.
  * You may obtain a copy of the License at
  *
  * http://www.apache.org/licenses/LICENSE-2.0
  *
  * Unless required by applicable law or agreed to in writing, software
  * distributed under the License is distributed on an "AS IS" BASIS,
  * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  * See the License for the specific language governing permissions and
  * limitations under the License.
  */

package ca.uwaterloo.cs451.project

import collection.mutable.HashMap
import io.bespin.scala.util.Tokenizer

import org.apache.log4j._
import org.apache.hadoop.fs._
import org.apache.spark.SparkContext
import org.apache.spark.SparkConf
import org.rogach.scallop._

object AllBigramCountDateAgnostic extends Tokenizer {
  val log = Logger.getLogger(getClass().getName())

  def main(argv: Array[String]) {
    val args = new AllBigramCountConf(argv)

    log.info("Input: " + args.input())
    log.info("Output: " + args.output())

    val conf = new SparkConf().setAppName("All Bigram Count Date Agnostic")
    val sc = new SparkContext(conf)
    val threshold = args.threshold()

    val outputDir = new Path(args.output())
    FileSystem.get(sc.hadoopConfiguration).delete(outputDir, true)

    val textFile = sc.textFile(args.input())

    def isAllDigits(x: String) = x forall Character.isDigit

    val counts = textFile
      .flatMap(line => {
        val lineSplit = line.split(",", -1)
        var text = ""
        var countryCode = ""

        if (lineSplit.length > 4){
          text = lineSplit(4).toLowerCase()
        }
        if (lineSplit.length > 13) {
          countryCode = lineSplit(13)
        }

        val tokens = tokenize(text)
        
        if (tokens.length > 1) tokens.sliding(2).map(p => p.mkString(" ")).map(bigram => ((countryCode, bigram), 1)).toList else List()
      })
      .filter(kvp => kvp._1._1 == "CA")
      .map(kvp => (kvp._1._2, kvp._2))
      .reduceByKey(_ + _)
      .filter(kvp => kvp._2 >= threshold)
      .map(kvp => (kvp._2, kvp._1))
      .sortByKey(false, 1)
      .take(100)

    sc.parallelize(counts).saveAsTextFile(args.output())
  }
}
