(ns aoc.2023-d01-p1
  (:require [clojure.string :as str]))

(def sample-input "1abc2\npqr3stu8vwx\na1b2c3d4e5f\ntreb7uchet\n")
(def input (slurp "src/aoc/2023_d01.txt"))

(defn solve [data]
  (let [lines (str/split-lines data)]
    (->> lines
         (map #(re-seq #"\d" %))
         (map #(str (first %) (last %)))
         (map #(Integer/parseInt %))
         (reduce +))))

(solve input)
