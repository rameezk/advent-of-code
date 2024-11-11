(ns aoc.2023-d02-p1
  (:require [clojure.string :as str]))

(def sample-input "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green")

(def input (slurp "../inputs/2023_d02.txt"))

(def max-counts {:red 12
                 :green 13
                 :blue 14})

(defn get-color-count [set color]
  "Get the count of a color in a set. If no count is found 0 is explicitly returned."
  (let [color-count (last
          (re-find (re-pattern (str "(\\d+) " color)) set))]
    (if (nil? color-count)
      0
      (Integer/parseInt color-count))))

(defn parse-set [set]
  "Parse a set of a game and return a map of color counts"
  (let [blue-count (get-color-count set "blue")
        red-count (get-color-count set "red")
        green-count (get-color-count set "green")]
    {:blue  blue-count
     :red   red-count
     :green green-count}))

(defn set-possible? [set-counts]
  (every?
    (fn
      [[color count]]
      (<= count (get max-counts color)))
    (seq set-counts)))

(defn game-possible? [game-sets]
  (every? set-possible? game-sets))

(defn parse-game [game]
  (let [game-id (last
                  (re-find #"Game (\d+):" game))
        game-sets (map
                    #(parse-set %)
                    (str/split game #";"))]
    (if
      (game-possible? game-sets)
      (Integer/parseInt game-id)
      0)))

(defn solve [input]
  (->> (str/split-lines input)
       (map parse-game)
       (reduce +)))

(solve input)