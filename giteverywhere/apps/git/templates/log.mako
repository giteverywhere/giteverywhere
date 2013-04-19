<%inherit file="/base.mako"/>

<%def name="title()">
The git app
</%def>

<div>
  <h1>Viewing commit log for repository: ${repository_name}</h1>
  
  <table>
    <tr class="tr_heading">
      <th>Commit Hash</th>
      <th>Author</th>
      <th>Date & Time</th>
      <th>Commit Message</th>
    </tr>
    %for commit in commit_log:
    <tr class="${loop.cycle('oddrow', 'evenrow')}">
      <td>${commit['commit_hash']}</td>
      <td>${commit['author']}</td>
      <td>${commit['datetime']}</td>
      <td>${commit['message'].replace("\n", "<br />\n") | n}</td>
    </tr>
    %endfor
  </table>
  
</div>
