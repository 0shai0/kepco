package com.example.mybatis.mapper;

import org.apache.ibatis.annotations.Mapper;
import java.util.*;

@Mapper
public interface DemoMapper{
    public List<Map<String,Object>> select();

    public List<Map<String,Object>> selectById(String seq);

    public void insert(String seq, String user);
    public void update(String seq, String user);
    public void delete(String seq);
}
