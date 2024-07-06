package com.course.springai_structured_output_chat_client.dto;

public record BooksInfo(
        String category,
        String book,
        String year,
        String review,
        String author,
        String summary
) {};
