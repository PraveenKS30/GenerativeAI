package com.example.springaivectorsearchdemo.services;

import org.springframework.ai.document.Document;

import org.springframework.ai.vectorstore.SearchRequest;
import org.springframework.ai.vectorstore.VectorStore;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Map;

@Service
public class VectorServices {

    @Autowired
    VectorStore vectorStore;


    public List<Document> simpleVector(String query){
        List<Document> documents = List.of(
                new Document("Spring AI rocks!! Spring AI rocks!! Spring AI rocks!! Spring AI rocks!! Spring AI rocks!!", Map.of("meta1", "meta1")),
                new Document("The World is Big and Salvation Lurks Around the Corner"),
                new Document("The World is Big"),
                new Document("You walk forward facing the past and you turn back toward the future.", Map.of("meta2", "meta2")));

        //add documents to the vector store
        vectorStore.add(documents);


        // retrieve documents similar to the given query
        List<Document> results = vectorStore.similaritySearch(
                SearchRequest.defaults()
                        .withQuery(query)
                        .withTopK(2)
        );
        return results;
    }

}
