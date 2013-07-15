 
<%inherit file="/base.mako"/>

<%def name="title()">
The git app
</%def>

<div>
  <h1>Viewing commit log differences for repository: ${repository_name}</h1>
  
  <table>
    <tr class="tr_heading">
      <th>Commit Hash</th>
      <th>Author</th>
      <th>Date & Time</th>
      <th>Commit Message</th>
      <th>File Name</th>
      <th>Changes</th>
      <th bgcolor="#5D7B9D" color="#FFFFFF"><font color="#FFFFFF">Header 1</font></th>
    </tr>
    %for diff in view_diff:
    <tr class="${loop.cycle('oddrow', 'evenrow')}">
      <td>${diff['commit_hash']}</td>
      <td>${diff['author']}</td>
      <td>${diff['datetime']}</td>
      <td>${diff['message']}</td>
      <td>${diff['file_name']}</td>
      <td>${diff['changes'].replace("\n", "<br />\n") | n}</td>
    </tr>
    %endfor
  </table>
  
</div>
