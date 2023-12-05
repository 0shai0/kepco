package com.example.board.mapper;

import org.apache.ibatis.annotations.Mapper;

import java.util.*;


@Mapper
public interface DemoMapperById {
    public List<Map<String, Object>> selectById(String seq);
}


