<h1>Resultat</h1>

<form action="http://localhost:9999/" methode="GET">
<INPUT TYPE="submit" NAME="nom" VALUE="Nouvelle recherche">
</FORM>

<table>
<tr><th>Nom equipement</th><th>Nom installation</th><th>Adresse</th><th>CP</th><th>Ville</th><th>Map</th></tr>
%for row in rows:
    <tr>

        <td>{{row[0]}}</td>
        <td>{{row[1]}}</td>
        <td>{{row[2]}}</td>
        <td>{{row[3]}}</td>
        <td>{{row[4]}}</td>

    <td><a href="http://localhost:9999/recherche/map?lat={{row[5]}}&long={{row[6]}}&ref={{row[4]}}"}>Afficher Map</a></td>
    </tr>
%end
</table>
