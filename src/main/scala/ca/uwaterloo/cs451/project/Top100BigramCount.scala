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

object Top100BigramCount extends Tokenizer {
  val log = Logger.getLogger(getClass().getName())

  def main(argv: Array[String]) {
    val args = new CustomConf(argv)

    log.info("Input: " + args.input())
    log.info("Output: " + args.output())

    val conf = new SparkConf().setAppName("Top 100 Bigram Count")
    val sc = new SparkContext(conf)

    val outputDir = new Path(args.output())
    FileSystem.get(sc.hadoopConfiguration).delete(outputDir, true)

    val textFile = sc.textFile(args.input())

    def isAllDigits(x: String) = x forall Character.isDigit

    val top100Bigrams = List("covid coronavirus", "in the", "of the", "this is", "coronavirus covid", "of covid", "to the", "thank you", "to be", "the covid", "on the", "covid covid", "for the", "the coronavirus", "is a", "to covid", "we are", "will be", "need to", "due to", "for covid", "is the", "the world", "social distancing", "to help", "at the", "all the", "right now", "coronavirus https://t.co/9zdojmiymo", "going to", "for a", "and the", "from the", "in a", "if you", "to get", "during this", "during covid", "covid pandemic", "to do", "i am", "this covid", "we can", "it is", "covid is", "i have", "to see", "with the", "the spread", "we need", "have a", "on covid", "stay home", "spread of", "out of", "you are", "at home", "during the", "you to", "with covid", "we have", "toilet paper", "they are", "have to", "in this", "one of", "to all", "people are", "have been", "time to", "is not", "for all", "covid and", "you can", "to keep", "as a", "and i", "about the", "who are", "want to", "all of", "covid in", "about covid", "trying to", "the same", "of a", "a great", "i think", "be a", "stay safe", "to go", "should be", "has been", "you have", "covid covid19canada", "in canada", "to make", "of this", "covid socialdistancing", "of our")

    val broadcastVar = sc.broadcast(top100Bigrams)

    // 12 is the retween count
    // 4 is the text
    val counts = textFile
      .flatMap(line => {
        val lineSplit = line.split(",", -1)
        var createdAt = ""
        var text = ""
        var retweetCount = 0
        var countryCode = ""

        if (lineSplit.length > 2) {
          createdAt = lineSplit(2).slice(0, 10)
        }
        if (lineSplit.length > 4){
          text = lineSplit(4).toLowerCase()
        }
        if (lineSplit.length > 13) {
          countryCode = lineSplit(13)
        }

        val tokens = tokenize(text)
        if (tokens.length > 1) tokens.sliding(2).map(p => p.mkString(" ")).map(bigram => ((countryCode, bigram, createdAt), 1)).toList else List()
      })
      .filter(kvp => kvp._1._3.matches("[0-9]{4}-[0-9]{2}-[0-9]{2}") && broadcastVar.value.contains(kvp._1._2))
      .map(kvp => ((kvp._1._2, kvp._1._3), kvp._2))
      .reduceByKey(_ + _)
      .sortByKey(true, 1)

    counts.saveAsTextFile(args.output())
  }
}
