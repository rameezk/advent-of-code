(ns aoc.2023-d03-p1
  (:require [clojure.string :as str]))

(def sample-input "467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..")

(def input (slurp "../inputs/2023_d03.txt"))

(def splitted-lines
  (str/split-lines sample-input))

splitted-lines

(defn indexes-of-symbols [line]
  (keep-indexed
    (fn
      [idx char]
      (when
        (re-find #"[^0-9.]" (str char)) idx))
    line))


(defn get-symbol-positions [lines]
  (apply concat
         (map-indexed
           (fn
             [row-idx row-line]
             (->> (indexes-of-symbols row-line)
                  (map #(vector row-idx %))))
           lines)))

(defn get-adjacent-coords [[x y]]
  (for [dx [-1 0 1]
        dy [-1 0 1]
        :when (not= dx dy 0)]
    [(+ x dx) (+ y dy)]))

(defn get-char-at [lines coord]
  (get-in lines coord))

(let [lines (str/split-lines sample-input)
      symbol-positions (get-symbol-positions lines)]
  (->> symbol-positions
       (map get-adjacent-coords)))




