package com.course.springai_openai_function_calling.dto;

public class Weather {

    public record Request(String city){}
    public record Response(Location location, Current current){}
    public record Location(String name, String country){}
    public record Current(String temp_c){}

}
