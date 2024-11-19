package me.rameezkhan.aoc

import java.io.File

val sample_input = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
""".trimIndent()

val real_input = File("inputs/2023_d1.txt").readText().trimIndent()

fun getDigit(line: String): Long {
    val matches = Regex("""\d""").findAll(line)
    val digit = matches.first().value + matches.last().value
    return digit.toLong()
}

fun main(args: Array<String>) {
    val lines = real_input.split("\n")
    val digits = lines.map { getDigit(it) }
    val total = digits.sum()
    println(total)
}