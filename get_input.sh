#!/usr/bin/env bash

session_cookie=$(cat .session-cookie)

read -p "year: " year
read -p "day: " day

curl -Lo "inputs/${year}_d${day}.txt" "https://adventofcode.com/$year/day/$day/input" -H "Cookie: session=$session_cookie"
