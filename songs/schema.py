import graphene
from graphene_django import DjangoObjectType
from .models import *
from graphene_django.filter import DjangoFilterConnectionField


class ArtistNode(DjangoObjectType):
    class Meta:
        model = Artist
        filter_fields = {'name': {'exact', 'startswith', 'contains'}}
        interfaces = (graphene.relay.Node,)


class BandNode(DjangoObjectType):
    class Meta:
        model = Band
        filter_fields = {'name': {'exact', 'startswith', 'contains'}}
        interfaces = (graphene.relay.Node,)


class SongNode(DjangoObjectType):
    class Meta:
        model = Song
        filter_fields = {
            'name': {'exact', 'startswith', 'contains'},
            'genre': {'exact', 'startswith', 'contains'},
            'sub_genre': {'exact', 'startswith', 'contains'},
            'band__name': {'exact', 'startswith', 'contains'},
            'artist__name': {'exact', 'startswith', 'contains'},
            'tags': {'exact', 'startswith', 'contains'},
            'similar_bands': {'exact', 'startswith', 'contains'},
        }
        interfaces = (graphene.relay.Node,)


class Query(object):
    all_artists = DjangoFilterConnectionField(ArtistNode)
    all_bands = DjangoFilterConnectionField(BandNode)
    all_songs = DjangoFilterConnectionField(SongNode)
    artist = graphene.relay.Node.Field(ArtistNode)
    band = graphene.relay.Node.Field(BandNode)
    song = graphene.relay.Node.Field(SongNode)


class CreateArtist(graphene.ClientIDMutation):
    class Input:
        name = graphene.String(required=True)

    artist = graphene.Field(ArtistNode)
    ok = graphene.Boolean()

    def mutate_and_get_payload(self, info, name, client_id_mutation=None):
        artist = ArtistNode._meta.model(name=name)
        artist.save()
        return CreateArtist(artist=artist, ok=bool(artist.id))


class Mutation(graphene.ObjectType):
    create_artist = CreateArtist.Field()
