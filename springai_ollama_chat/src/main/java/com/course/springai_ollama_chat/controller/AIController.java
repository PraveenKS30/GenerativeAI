package com.course.springai_ollama_chat.controller;

import com.course.springai_ollama_chat.service.AIService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.io.IOException;

@RestController
@RequestMapping("/ai")
public class AIController {

    @Autowired
    AIService aiService;

    @PostMapping("/chat")
    public String getResponse(@RequestParam String category, String year){
        return aiService.getResponse(category, year);
    }

    @PostMapping("/ask")
    public String getResponse(@RequestBody String query){
        return aiService.getSummarizeText(query);
    }



    @GetMapping("/image/chat")
    public String getMultiModalResp() throws IOException {
        return aiService.getMultiModalResponse();
    }
}
