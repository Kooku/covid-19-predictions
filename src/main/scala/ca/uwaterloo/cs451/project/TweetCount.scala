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

class CustomConf(args: Seq[String]) extends ScallopConf(args) {
  mainOptions = Seq(input, output)
  val input = opt[String](descr = "input path", required = true)
  val output = opt[String](descr = "output path", required = true)
  verify()
}

object TweetCount {
  val log = Logger.getLogger(getClass().getName())

  def main(argv: Array[String]) {
    val args = new CustomConf(argv)

    log.info("Input: " + args.input())
    log.info("Output: " + args.output())

    val conf = new SparkConf().setAppName("Tweet Count")
    val sc = new SparkContext(conf)

    val outputDir = new Path(args.output())
    FileSystem.get(sc.hadoopConfiguration).delete(outputDir, true)

    val textFile = sc.textFile(args.input())

    val counts = textFile
      .map(line => {
        val lineSplit = line.split(",", -1)
        var createdAt = ""
        if (lineSplit.length > 2) {
          createdAt = lineSplit(2).slice(0, 10)
        }
        (createdAt, 1)
      })
      .filter(_._1.matches("[0-9]{4}-[0-9]{2}-[0-9]{2}"))
      .reduceByKey(_ + _)
      .sortByKey(true, 1)
      // .foreach(println)

    counts.saveAsTextFile(args.output())
  }
}
