package com.example.board.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class PageRequest {
    @GetMapping("/")
    public String home() {
        return "html/index";
    }
}
