# Monoku Test ‍🎶

### Query Songs
```
{
    allSongs {
        edges {
            node {
                id
                name
                tags
                genre
                band {
                    id
                    name
                }
                artist {
                    id
                    name
                }
            }
        }
    }
}

```

Songs can be filtered by: `name`, `tags`, `genre`, `sub genre`, and `similar_band`.
They can be found by the exact string or sub string

Eg. Exact string:
```
{ 
    allSongs(name: "Rope") {
    ...
}
```

Eg. Sub string:
```
{ 
    allSongs(name_Contains: "ope") {
    ...
}
```
or
```
{ 
    allSongs(name_Startswith: "Rop") {
    ...
}
```

### Query Artists
```
{
    allArtists {
        edges {
            node {
                id
                name
            }
        }
    }
}

```

### Query Bands
```
{
    allBands {
        edges {
            node {
                id
                name
            }
        }
    }
}

```

### Create Artist 
```
mutation {
  createArtist(input: {name: "Foo"}) {
    artist {
      name
      id
    }
  }
}
```