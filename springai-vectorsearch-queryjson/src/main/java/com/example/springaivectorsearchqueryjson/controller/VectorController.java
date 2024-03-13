package com.example.springaivectorsearchqueryjson.controller;

import com.example.springaivectorsearchqueryjson.services.VectorService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("api/v1")
public class VectorController {

    @Autowired
    VectorService vectorService;

    @GetMapping("/query")
    public String getQueryResults(@RequestParam String query){
        return vectorService.queryJSONVector(query).get(0).getMetadata().toString();
    }
}
