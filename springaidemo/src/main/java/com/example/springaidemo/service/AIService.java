package com.example.springaidemo.service;

import org.springframework.ai.client.AiClient;
import org.springframework.ai.client.AiResponse;
import org.springframework.ai.prompt.PromptTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class AIService {

    @Autowired
    AiClient aiClient;

    public String getJoke(String topic){
        PromptTemplate promptTemplate = new PromptTemplate("""
                Please act as a funny person and  create a joke on the given {topic}?
                Please be mindful and sensitive about the content though.
               """);
        promptTemplate.add("topic", topic);
        return this.aiClient.generate(promptTemplate.create()).getGeneration().getText();
    }

    // generate output in the JSON format
    public String getBooks(String category, String year){
        PromptTemplate promptTemplate = new PromptTemplate("""
                Please provide me best book for the given {category} and the {year}.
                Please do provide a summary of the book as well, the information should be 
                limited and not much in depth. Please provide the details in the JSON format
                containing this information : category, year, review, author, summary
                """);
         promptTemplate.add("category", category);
         promptTemplate.add("year", year);
         AiResponse generate = this.aiClient.generate(promptTemplate.create());
         return generate.getGeneration().getText();
    }
}
