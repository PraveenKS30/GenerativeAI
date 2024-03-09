package com.example.springaivectorsearchdemo.config;
import org.springframework.ai.embedding.EmbeddingClient;
import org.springframework.ai.vectorstore.SimplePersistentVectorStore;
import org.springframework.ai.vectorstore.VectorStore;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class VectorStoreConfig {

    @Bean
    VectorStore vectorStore(EmbeddingClient embeddingClient){
        return new SimplePersistentVectorStore(embeddingClient);
    }
}
