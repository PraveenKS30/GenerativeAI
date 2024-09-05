package com.course.springai_openai_function_calling.service;

import com.course.springai_openai_function_calling.dto.Weather;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestClient;
import org.springframework.web.util.UriComponentsBuilder;

@Service
public class WeatherServieBuilder {

    @Value("${spring.weather.api.base.uri}")
    private String weatherBaseURI ;

    @Value("${spring.weather.api.key}")
    private String weatherAPIKey ;


    private RestClient restClient = RestClient.create();

    public Weather.Response getWeather(String city){
        return restClient.get()
                .uri(UriComponentsBuilder.fromUriString(weatherBaseURI)
                        .path("/current.json")
                        .queryParam("key", weatherAPIKey)
                        .queryParam("q", city) // Replace with the actual city
                        .toUriString())
                .retrieve()
                .body(Weather.Response.class);
    }

}
