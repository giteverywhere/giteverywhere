<%inherit file="/base.mako"/>

<%def name="title()">
The git app
</%def>

<div>
       
  <table>
    <tr class="tr_heading">
      <th>Is_First </th>
      <th>Is_Last</th>
      <th>Commit Hash</th>
      <th>Author</th>
      <th>Date & Time</th>
      <th>Commit Message</th>
    </tr>
  
%if output == 'html':
 
    %for commit in comit_log:
    <tr class="${loop.cycle('oddrow', 'evenrow')}">
      <td>${commit['is_first']}</td>
      <td>${commit['is_last']}</td>
      <td>${commit['commit_hash']}</td>
      <td>${commit['author']}</td>
      <td>${commit['datetime']}</td>
      <td>${commit['message'].replace("\n", "<br />\n") | n}</td>
      <td><a href="${request.route_url('git.cdiff', repo=repo, hash=commit['commit_hash'])}">Difference</a></td>   
    </tr>
    %endfor
    
%elif output == 'json':
  <table>
      <tr>
        <td>${data}</td>
      </tr>      
%endif
  </table>  
</div>
