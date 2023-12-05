package com.example.mybatis.mapper;

import org.apache.ibatis.annotations.Mapper;
import java.util.*;

@Mapper
public interface BoardMapper {
    public List<Map<String,Object>> selectList();
    public List<Map<String,Object>> selectDetail(String seq);
    public void insertBoard(String title, String content, String writer, String writeDate);


public void updateBoard(
    String seq,
    String title,
    String content,
    String writeDate
);

};
