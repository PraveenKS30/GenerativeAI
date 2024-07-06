package com.course.springai_structured_output_chat_client.controller;

import com.course.springai_structured_output_chat_client.dto.BooksInfo;
import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.converter.ListOutputConverter;
import org.springframework.ai.converter.MapOutputConverter;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.ParameterizedTypeReference;
import org.springframework.core.convert.support.DefaultConversionService;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.lang.reflect.Type;
import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/ai")
public class AIChatController {

   private final ChatClient chatClient;

   public AIChatController(ChatClient.Builder chatClient){
       this.chatClient = chatClient.build();
   }

    // using Prompt and JSON object
    @PostMapping("/v0/chat")
    public  String getResponse(@RequestParam String category, String year){
        return chatClient.prompt()
                .user(u-> u.text("Please provide the book details for the given {category} and {year} in the JSON format.")
                        .param("category", category)
                        .param("year", year))
                .call()
                .content();
    }

    //using BeanOutputConverter
    @PostMapping("/v1/chat")
    public BooksInfo getBeanResponse(@RequestParam String category, String year){
         return chatClient.prompt()
                 .user(u-> u.text("Please provide the book details for the given {category} and {year}.")
                         .param("category", category)
                         .param("year", year))
                 .call()
                 .entity(BooksInfo.class);
     }

     // ParameterizedTypeReference to handle generic case
    @PostMapping("/v2/chat")
    public List<BooksInfo> getListBeanResponse(@RequestParam String category, String year){
        return chatClient.prompt()
                .user(u-> u.text("Please provide 2 book details for the given {category} and {year}.")
                        .param("category", category)
                        .param("year", year))
                .call()
                .entity(new ParameterizedTypeReference<List<BooksInfo>>() {
                });
    }

    // using ListOutputConverter
    @PostMapping("/v3/chat")
    public List<String> getListResponse(@RequestParam String category, String year){
        return chatClient.prompt()
                .user(u-> u.text("Please provide the names of  5 best books for the given {category} and the {year}")
                        .param("category", category)
                        .param("year", year))
                .call()
                .entity(new ListOutputConverter(new DefaultConversionService()));
    }

    // using MapOutputConverter
    @PostMapping("/v4/chat")
    public Map<String, Object> getMapResponse(@RequestParam String category, String year){
        return chatClient.prompt()
                .user(u-> u.text("Please provide me best book for the given {category} and the {year}.\n" +
                                "                Please do provide a summary of the book as well, the information should be \n" +
                                "                limited and not much in depth. The response should be in the JSON format " +
                                "                containing this information:\n" +
                                "                category, book, year, review, author, summary" +
                                "                Please remove ```json from the final output"
                                )
                        .param("category", category)
                        .param("year", year))
                .call()
                .entity(new ParameterizedTypeReference<Map<String, Object>>() {
                });
    }
}
