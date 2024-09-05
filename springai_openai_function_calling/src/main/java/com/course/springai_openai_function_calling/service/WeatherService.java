package com.course.springai_openai_function_calling.service;

import com.course.springai_openai_function_calling.dto.Weather;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.function.Function;

@Service
public class WeatherService implements Function<Weather.Request, Weather.Response > {

    @Autowired
    WeatherServieBuilder weatherServieBuilder;

    @Override
    public Weather.Response apply(Weather.Request request) {
        return weatherServieBuilder.getWeather(request.city());
    }
}
