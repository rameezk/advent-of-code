(ns aoc.2023-d01-p2
  (:require [clojure.string :as str]))

(def sample-input "two1nine\neightwothree\nabcone2threexyz\nxtwone3four\n4nineeightseven2\nzoneight234\n7pqrstsixteen\n")
(def input (slurp "src/aoc/2023_d01.txt"))

(def lookup
  {"one" 1
   "two" 2
   "three" 3
   "four" 4
   "five" 5
   "six" 6
   "seven" 7
   "eight" 8
   "nine" 9
   "1" 1
   "2" 2
   "3" 3
   "4" 4
   "5" 5
   "6" 6
   "7" 7
   "8" 8
   "9" 9})

(defn get-ordered-digits [line]
  (->> lookup
       (reduce
         (fn [result [search-for digit]]
           (let [position (str/index-of line search-for)
                 position-from-back (str/last-index-of line search-for)]
             (conj
               result
               (when (some? position) [position digit])
               (when (some? position-from-back) [position-from-back digit]))))
         [])
       (filter some?)
       (sort)
       (map second)))

(defn get-number [digits]
  (Integer/parseInt (str (first digits) (last digits))))

(defn solve [data]
  (let [lines (str/split-lines data)]
    (->> lines
         (map get-ordered-digits)
         (map get-number)
         (reduce +))))

(solve input)







