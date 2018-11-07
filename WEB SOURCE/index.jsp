<?xml version="1.0" encoding="UTF-8" ?>
<%@page import="org.apache.jasper.tagplugins.jstl.core.Catch"%>
<%@page import="java.io.IOException"%>
<%@page import="java.io.FileNotFoundException"%>
<%@page import="java.io.FileReader"%>
<%@page import="java.io.BufferedReader"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<title>Toilet log</title>
</head>
<body>
        <p class="auto-style1">Toilet enter log page</p>
        <p class="auto-style1">&nbsp;</p>
        <p class="auto-style1">&nbsp;</p>
        <p class="auto-style1">&nbsp;</p>
        <p class="auto-style1">&nbsp;</p>
 <%
    BufferedReader reader = null;
    String filePath = application.getRealPath("log.txt"); 
    reader = new BufferedReader(new FileReader(filePath));
    while(true)
    {
        String str = reader.readLine();  
        if(str==null)
        break;
        out.print(str+"</br>");    
    }
   reader.close();    
 %>
</body>
</html>
