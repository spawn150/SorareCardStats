from gql import gql

TeamPlayersQuery = gql(
    """
  query GetNbaTeamSlugs($team: String!){
    nbaTeam(slug: $team){
      id
      players{
        slug
        displayName
      }
    }
  }
"""
)

PlayerLastStatsQuery = gql(
    """
    query GetNbaPlayerLastStats($players: [String!]){
      nbaPlayers(slugs: $players) {
        id
        slug
        positions
        isActive
        team{
          name
        }
        latestFinalFixtureStats(last: 15){
          score
          fixture {
            fixtureState
          }
        }
        tenGameAverage
      }
    }
  """
)