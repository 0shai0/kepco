package com.example.board.config;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.context.annotation.Configuration;


@Configuration
@MapperScan(basePackages = "com.example.board.mapper")
public class MyBatisConfig {
    
}



// package com.example.board.mapper;

// import java.util.*;

// import org.apache.ibatis.annotations.Mapper;

// @Mapper
// public interface DemoMapper {
//     public List<Map<String, Object>> select();
    
// }