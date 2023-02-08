package org.ruifsp.kata6;

/*
John has invited some friends. His list is:

s = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill";
Could you make a program that

makes this string uppercase
gives it sorted in alphabetical order by last name.
When the last names are the same, sort them by first name. Last name and first name of a guest come in the
result between parentheses separated by a comma.

So the result of function meeting(s) will be:

"(CORWILL, ALFRED)(CORWILL, FRED)(CORWILL, RAPHAEL)(CORWILL, WILFRED)(TORNBULL, BARNEY)(TORNBULL, BETTY)(TORNBULL, BJON)"
It can happen that in two distinct families with the same family name two people have the same first name too.

Notes
You can see another examples in the "Sample tests".
 */

import java.util.*;

public class Meeting {
    public static String meeting(String s) {

        TreeMap<String, List<String>> people = new TreeMap<>();
        String[] persons = s.split(";");
        for(String person : persons){
            String[]  fullNames = person.split(":");
            String firstName = fullNames[1].toUpperCase();
            String secondName =  fullNames[0].toUpperCase();

            List<String> names;
            if(!people.containsKey( firstName )){
                names = new ArrayList<>();
                names.add(secondName);
            }else {
                names = people.get(firstName);
                names.add(secondName);
                Collections.sort(names);
            }
            people.put(firstName, names);

        }

        StringBuilder result = new StringBuilder();
        Set<String> secondNames = people.keySet();

        for(String secondName : secondNames ){
            List<String> names = people.get(secondName);
            for( String name  : names ){
                result.append("(").append(secondName.toUpperCase()).append(", ").append(name.toUpperCase()).append(")");
            }
        }
        return result.toString();
    }
}

/*

import java.util.Arrays;
import java.util.stream.Collectors;

function approach
    public static String meeting(String s) {
      return Arrays.stream(s.toUpperCase().split(";"))
                   .map(guest -> guest.replaceAll("(\\w+):(\\w+)", "($2, $1)"))
                   .sorted()
                   .collect(Collectors.joining(""));
    }
 */