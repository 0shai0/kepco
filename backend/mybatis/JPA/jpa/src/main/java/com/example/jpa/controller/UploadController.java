package com.example.jpa.controller;

import java.io.File;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;


@Controller
public class UploadController {
    @GetMapping("/upload1")
    public String upload1() {
        return "html/upload1";
    }

    @PostMapping("/upload1")
    @ResponseBody
    public String upload1Post(
        MultipartHttpServletRequest mRequest) {
            String result = "";
            MultipartFile mFile = mRequest.getFile("file") ;
            String oName = mFile.getOriginalFilename();
            result += oName + "<br>" + mFile.getSize();
            String saveFolder = "C:/data/";
            File saveFile = new File();
        return result;
    }

    public String 
}
