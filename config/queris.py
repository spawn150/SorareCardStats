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

#add 1 game more because it considers also next game with score 0
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
        latestThreeScores: latestFinalFixtureStats(last: 4){
          score
        }
        latestFiveScores: latestFinalFixtureStats(last: 6){
          score
        }
        tenGameAverage
      }
    }
  """
)