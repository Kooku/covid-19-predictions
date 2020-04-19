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

    val stopwords = List("i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now")
    val stopwordsB = sc.broadcast(stopwords)

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

        val tokens = tokenize(text).filter(word => !stopwordsB.value.contains(word))
        
        if (tokens.length > 1) tokens.sliding(2).map(p => p.mkString(" ")).map(bigram => ((countryCode, bigram), 1)).toList else List()
      })
      // .filter(kvp => kvp._1._1 == "CA")
      .map(kvp => (kvp._1._2, kvp._2))
      .reduceByKey(_ + _)
      .filter(kvp => kvp._2 >= threshold)
      .map(kvp => (kvp._2, kvp._1))
      .sortByKey(false, 1)
      .take(1000)

    sc.parallelize(counts).saveAsTextFile(args.output())
  }
}
