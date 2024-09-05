package com.course.springai_openai_function_calling.controller;

import com.course.springai_openai_function_calling.service.AIService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.Map;

@RestController
@RequestMapping("/ai")
public class AIController {

    @Autowired
    AIService aiService;

    @PostMapping("/query")
    public Map<String, String> getWeatherDetails(@RequestParam String query){
        return Map.of("response", aiService.getWeatherInfo(query).getResult().getOutput().getContent());
    }
}
