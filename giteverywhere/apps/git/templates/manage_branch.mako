<%inherit file="/base.mako"/>

<%def name="title()">
The git app
</%def>

<div>
  <h1>Branches of ${repo}</h1>
    <a href ="${request.route_url('git.clog')}">Commits</a>&nbsp;&nbsp;&nbsp;&nbsp;
     
    <a href="${request.route_url('git.branch')}">Branches</a> 
  
  <table>
    <tr class="tr_heading">

      <th>Branch name</th>
      <th>Commit Hash</th>
      <th>Author</th>
      <th>Date & Time</th>
      <th>Commit Message</th>
    </tr>
   
   %for branch in branch_view:
   <tr class="${loop.cycle('oddrow', 'evenrow')}">
   <td>${branch['branch_name']}</td>
     %endfor
    %for commit in commit_log:
    <class="${loop.cycle('oddrow', 'evenrow')}">
      <td>${commit['commit_hash']}</td>
      <td>${commit['author']}</td>
      <td>${commit['datetime']}</td>
      <td>${commit['message'].replace("\n", "<br />\n") | n}</td>
      %endfor

    </tr>
  
 
  </table>
  
    <h1>Viewing all tags of repository: ${repo}</h1>
  <table>
    <tr class="tr_heading">
      <th>Tags</th>
    </tr>
   %for tag in tag_list:
   <tr class="${loop.cycle('oddrow', 'evenrow')}">
   <td>${tag['tag_title']}</td>
      </tr>
      %endfor  
  </table>
  
  
  <h1>Viewing last tag detail of repository: ${repo}</h1>
  <table>
    <tr class="tr_heading">
      <th>Tags</th>
    </tr>
   %for tag in tag_show:
   <tr class="${loop.cycle('oddrow', 'evenrow')}">
   <td>${tag['tag_title']}</td>
      </tr>
      %endfor  
  </table>
  
 
 
   
  
  
</div>
