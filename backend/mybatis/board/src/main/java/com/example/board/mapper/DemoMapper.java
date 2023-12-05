package com.example.board.mapper;

import java.util.*;

import org.apache.ibatis.annotations.Mapper;

@Mapper
public interface DemoMapper {
    public List<Map<String, Object>> select();
    
}