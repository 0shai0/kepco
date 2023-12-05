package com.example.board.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.*;
import com.example.board.mapper.DemoMapper;

@RestController

public class DBController {
    @Autowired
    DemoMapper demoMapper;
    

    @GetMapping("/mybatis/demo")
    public List<Map<String,Object>> mybatisDemo() {
        return demoMapper.select();
    }

    // @Autowired
    // DemoMapper demoMapper1;

    // @GetMapping("/mybatis/demoid")
    // public List<Map<String,Object>> mybatisDemoById() {
    //     return demoMapper1.selectById("1");
    // }

}
