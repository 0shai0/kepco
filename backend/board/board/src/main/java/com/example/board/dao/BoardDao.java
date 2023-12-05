package com.example.board.dao;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Repository;
import java.util.*;

@Repository
public class BoardDao {
    @Autowired
    JdbcTemplate jt;

    public List<Map<String,Object>> listSelect() {
        String sqlStmt = "select seq, title, content, writer, search_count from board";
        return jt.queryForList(sqlStmt);
    }

    public void insert(String title, String content, String writer) {
        String sqlStmt = String.format("INSERT INTO BOARD(title, content, writer) values('%s','%s','%s')", title, content, writer);
        jt.execute(sqlStmt);
    }

    public List<Map<String,Object>> detatilSelect(String seq) {
        String sqlStmt = String.format("select content,title, search_count from board where seq = %s", seq);
        return jt.queryForList(sqlStmt);
    }

    public void delete(String seq) {
        String sqlStmtMain = String.format("delete from board where seq = '%s'", seq);
        String sqlStmtDetail = String.format("delete from board_answer where seq = '%s'", seq);
        //database 설정이 더 좋음 (foreign-key cascade)
        
        jt.queryForList(sqlStmtMain);
        jt.queryForList(sqlStmtDetail);
    }

    public void update(String title, String content, String seq) {
        String sqlStmt = String.format("UPDATE board SET title ='%s', content='%s' where seq = '%s'",title, content, seq);
        jt.queryForList(sqlStmt);
    }

    public void UpdateSearchCount(String seq, String searchCount) {
        String sqlStmt = String.format("update board set search_count = '%s' where seq = %s", searchCount,seq);
        jt.queryForList(sqlStmt);
    }

    public void insertAnswer(String seq, String answer) {
        String sqlStmt = String.format("INSERT INTO board_answer(seq, answer) VALUES(%s,'%s')", seq,answer);
        jt.queryForList(sqlStmt);
    }

    public List<Map<String, Object>> getCountAnswer(String seq) {
        String sqlStmt = String.format("select answer from board_answer where seq = %s", seq);
        return jt.queryForList(sqlStmt);
    }

}


