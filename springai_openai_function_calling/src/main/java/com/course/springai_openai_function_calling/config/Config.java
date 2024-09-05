package com.course.springai_openai_function_calling.config;

import com.course.springai_openai_function_calling.dto.Weather;
import com.course.springai_openai_function_calling.service.WeatherService;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Description;

import java.util.function.Function;

@Configuration
public class Config {

    @Bean
    @Description("Get the weather of the city")
    Function<Weather.Request, Weather.Response> currentWeather(){
        return new WeatherService();
    }
}
