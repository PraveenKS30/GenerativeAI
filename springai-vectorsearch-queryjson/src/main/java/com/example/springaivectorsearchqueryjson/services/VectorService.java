package com.example.springaivectorsearchqueryjson.services;

import org.springframework.ai.document.Document;
import org.springframework.ai.reader.JsonMetadataGenerator;
import org.springframework.ai.reader.JsonReader;
import org.springframework.ai.vectorstore.SearchRequest;
import org.springframework.ai.vectorstore.VectorStore;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.core.io.Resource;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Map;

@Service
public class VectorService {

    @Autowired
    VectorStore vectorStore;

    @Value("classpath:/data/bikes.json")
    Resource bikesResouce;

    public List<Document> queryJSONVector(String query){

        // read json file
        JsonReader jsonReader = new JsonReader(bikesResouce, new ProductMetadataGenerator(),
                "name","shortDescription", "description", "price","tags");

        // create document object
        List<Document> documents = jsonReader.get();

        // add to vectorstore
        vectorStore.add(documents);

        // query vector search
        List<Document> results = vectorStore.similaritySearch(
                SearchRequest.defaults()
                        .withQuery(query)
                        .withTopK(1)
        );

        return results ;
    }


    public class ProductMetadataGenerator implements JsonMetadataGenerator {

        @Override
        public Map<String, Object> generate(Map<String, Object> jsonMap) {
            return Map.of("name", jsonMap.get("name"),
                    "shortDescription", jsonMap.get("shortDescription"));
        }

    }
}
