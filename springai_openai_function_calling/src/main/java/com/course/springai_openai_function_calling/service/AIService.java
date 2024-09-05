package com.course.springai_openai_function_calling.service;

import org.springframework.ai.chat.messages.UserMessage;
import org.springframework.ai.chat.model.ChatModel;
import org.springframework.ai.chat.model.ChatResponse;
import org.springframework.ai.chat.prompt.Prompt;
import org.springframework.ai.openai.OpenAiChatOptions;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class AIService {

    @Autowired
    ChatModel chatModel;

    public ChatResponse getWeatherInfo(String query){

        UserMessage userMessage = new UserMessage(query);

        return chatModel.call(new Prompt((userMessage),
                OpenAiChatOptions.builder().withFunction("currentWeather").build()));

    }
}
