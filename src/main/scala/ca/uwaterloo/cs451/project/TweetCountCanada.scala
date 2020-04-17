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

import org.apache.log4j._
import org.apache.hadoop.fs._
import org.apache.spark.SparkContext
import org.apache.spark.SparkConf
import org.rogach.scallop._

object TweetCountCanada {
  val log = Logger.getLogger(getClass().getName())

  def main(argv: Array[String]) {
    val args = new CustomConf(argv)

    log.info("Input: " + args.input())
    log.info("Output: " + args.output())

    val conf = new SparkConf().setAppName("Tweet Count Canada")
    val sc = new SparkContext(conf)

    val outputDir = new Path(args.output())
    FileSystem.get(sc.hadoopConfiguration).delete(outputDir, true)

    val textFile = sc.textFile(args.input())

    val counts = textFile
      .map(line => {
        val lineSplit = line.split(",", -1)
        var createdAt = ""
        var countryCode = ""

        if (lineSplit.length > 2) {
          createdAt = lineSplit(2).slice(0, 10)
        }
        if (lineSplit.length > 13) {
          countryCode = lineSplit(13)
        }
        ((createdAt, countryCode), 1)
      })
      .filter(kvp => kvp._1._1.matches("[0-9]{4}-[0-9]{2}-[0-9]{2}") && kvp._1._2 == "CA")
      .map(kvp => (kvp._1._1, kvp._2))
      .reduceByKey(_ + _)
      .sortByKey(true, 1)

    counts.saveAsTextFile(args.output())
  }
}
