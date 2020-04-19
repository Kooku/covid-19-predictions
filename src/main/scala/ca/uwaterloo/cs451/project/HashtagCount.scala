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

object HashtagCount extends Tokenizer {
  val log = Logger.getLogger(getClass().getName())

  def main(argv: Array[String]) {
    val args = new CustomConf(argv)

    log.info("Input: " + args.input())
    log.info("Output: " + args.output())

    val conf = new SparkConf().setAppName("Hashtag Count")
    val sc = new SparkContext(conf)

    val outputDir = new Path(args.output())
    FileSystem.get(sc.hadoopConfiguration).delete(outputDir, true)

    val textFile = sc.textFile(args.input())

    val counts = textFile
      .map(line => {
        val lineSplit = line.split(",")
        var key = ""
        if (lineSplit.length > 1) {
          key = lineSplit(1)
        }
        (key, 1)
      }) 
      .filter(_._1 != "")
      .reduceByKey(_ + _)
      .map(kvp => (kvp._2, kvp._1))
      .sortByKey(false, 1)
      .map(kvp => (kvp._2, kvp._1))
      .take(100)

    sc.parallelize(counts).saveAsTextFile(args.output())
  }
}
