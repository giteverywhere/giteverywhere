 
 <%inherit file="/base.mako"/>

<%def name="title()">
The git app
</%def>

<div>
  <h1>Viewing branch view of repository: ${repository_name}</h1>
  
  <table>
    <tr class="tr_heading">
      <th>Branch name</th>

    </tr>
   %for branch in branches_names:
   <tr class="${loop.cycle('oddrow', 'evenrow')}">
   <td>${branch}</td>
      </tr>
      %endfor  
  </table>
   <table>
    <tr class="tr_heading">
      <th>Branch Name</th>
      <th>Commit Hash</th>
      <th>Author</th>
      <th>Date & Time</th>
      <th>First Commit</th>
      <th>Last Commit</th>
      <th>Commit Message</th>

    </tr>
    %for commit in diagram_record:
     
    <tr class="${loop.cycle('oddrow', 'evenrow')}">
      <td>${commit['branches']}</td>
      <td>${commit['commit_hash']}</td>
      <td>${commit['author']}</td>
      <td>${commit['datetime']}</td>
      <td>${commit['is_first']}</td>
      <td>${commit['is_last']}</td>
      <td>${commit['message'].replace("\n", "<br />\n") | n}</td>
     
    </tr>
      
    %endfor
  </table>
  
</div>


