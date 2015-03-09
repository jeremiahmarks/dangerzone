#!/usr/bin/ruby
# @Author: Jeremiah Marks
# @Date:   2015-03-08 17:22:54
# @last Modified 2015-03-08
# @last Modified time: 2015-03-08 18:07:13


def meeusJulianalgorithm(year)
    # from http://en.wikipedia.org/wiki/Computus#Meeus_Julian_algorithm
    val1 = year % 4
    val2 = year % 7
    val3 = year % 19
    val4 = (19*val3 + 15) %30
    val5 = ( 2* val1 + 4* val2 - val4 + 34)%7
    month = ((val4 + val5 + 114)/31.0).floor
    day = ((val4 + val5 + 114)%31)+1
    dateStr = day.to_s
    if month == 3
        dateStr << "March"
    else
        dateStr << "April"
    end
    dateStr << year.to_s

    puts dateStr
end

def anonymousGregorianalgorithm(year)
    # from http://en.wikipedia.org/wiki/Computus#Anonymous_Gregorian_algorithm
    a =  year % 19
    b = (year / 100.0).floor
    c = year % 100
    d = (b / 4.0).floor
    e = b % 4
    f = ((b + 8) / 25.0).floor
    g = ( ( b - f + 1 ) / 3.0).floor
    h = (19 * a + b - d - g + 15) % 30
    i = (c / 4.0).floor
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = ((a + 11*h + 22*l) / 451.0).floor
    month = ((h + l - 7*m + 114) / 31.0).floor
    day = ((h + l - 7*m + 114) % 31) + 1
    dateStr = day.to_s
    if month == 3
        dateStr << " March "
    else
        dateStr << " April "
    end
    dateStr << year.to_s
    puts dateStr
end

years = (2015..2025).to_a

years.each do |ayear|
    # puts "jul\t"
    # meeusJulianalgorithm(ayear)
    # puts "anon\t"
    anonymousGregorianalgorithm(ayear)
end
