package com.example.jpa.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import com.example.jpa.model.Demo;
import com.example.jpa.repository.DemoRepository;
import java.util.*;


@RestController
public class DBController {
    @Autowired
    DemoRepository demoRepository;
    @GetMapping("/")
    public List<Demo> demoSelect() {
        return demoRepository.findAll();
    }

    // @GetMapping("/user")
    // public String demoSelect1(){
    //     String user = demoRepository.findByUser("AAA").getUser();
    //     return user;
    // }

    // @GetMapping("/user1")
    // public Demo demoSelect2() {
    //     return demoRepository.findByUser("AAA");
    // }

    // @GetMapping("/user2")
    // public List<Demo> demoSelect3() {
    //     return demoRepository.findBySeq(2);
    // }


    @GetMapping("/save")
    public String demoInsert() {
        Demo data = new Demo();
        data.setSeq(4);
        data.setUser("이재빈");
        demoRepository.save(data);

        return "잘 저장되었습니다";
    }


    @GetMapping("/delete")
    public String demoDelete() {
        Demo data = new Demo();
        data.setSeq(4);
        demoRepository.delete(data);
        return "잘 지워졌습니다";
    }
}
