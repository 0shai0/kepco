package com.example.mybatis.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import com.example.mybatis.mapper.BoardMapper;
import java.util.*;
import java.time.LocalDate;
import java.time.LocalTime;

@RestController

public class DBController {
    
    @Autowired
    BoardMapper boardMapper;

 
    @GetMapping("/mybatis/boardselect")
    public List<Map<String,Object>> boardSelect() {
        return boardMapper.selectList();
    }

    @GetMapping("board/detail")
    public List<Map<String,Object>> boardDetail() {
        String seq = "9";
        return boardMapper.selectDetail(seq);
    }

    @GetMapping("board/insert")
    public String boardInsert(){
        String date = LocalDate.now().toString();
        String time = LocalTime.now().toString().substring(0,5);
        String writeDate = String.format("%s %s", date, time);
        String title = "오늘 아침 기온";
        String content = "매우 추웠음.. 특히 광주는";
        String writer = "이재빈";
        boardMapper.insertBoard(title, content, writer, writeDate);
        return writeDate + "에 잘 저장되었습니다";
    }

    @GetMapping("board/update")
    public String boardUpdate() {
        String date = LocalDate.now().toString();
        String time = LocalTime.now().toString().substring(0,5);
        String writeDate = String.format("%s %s", date, time);
        String seq = "1";
        String title = "오늘 아침 기온";
        String content = "매우 추웠음.. 특히 광주는";
        boardMapper.updateBoard(seq, title, content, writeDate);
        return writeDate + "에 잘 저장되었습니다";
    }
}
