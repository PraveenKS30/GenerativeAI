package com.example.springaivectorsearchdemo.controller;

import com.example.springaivectorsearchdemo.services.VectorServices;
import org.springframework.ai.document.Document;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;
import java.util.stream.Collectors;

@RestController
@RequestMapping("api/v1")
public class VectorController {

    @Autowired
    VectorServices vectorServices;

    @GetMapping("/gen")
    public String genVectorSearch(@RequestParam String query) {
        return vectorServices.simpleVector(query).get(0).getContent().toString();
    }


}
