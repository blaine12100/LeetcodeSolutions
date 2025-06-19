/*
https://leetcode.com/problems/movie-rating/description/?envType=study-plan-v2&envId=top-sql-50

Join Movietable (fact) to dimension tables (user and movie). Then, create 2 different CTE's. One for getting the highest user name rating wise. Save the op as resuts.

Then, create a different CTE to get the highest rated movie. Name it as results too.

Lastly, do a union by name to get both the results together
*/

# CTE for user who has rated more movies
With abc as (
select u.name as results from MovieRating as mr left join users as u on 
mr.user_id = u.user_id
group by mr.user_id
order by count(*) desc, u.name asc
limit 1
),

# CTE for getting the highest average rated movie in feb 2020
def as (
select m.title as results from MovieRating as mr left join movies as m on 
mr.movie_id = m.movie_id
where mr.created_at >= '2020-02-01' and mr.created_at < '2020-03-01'
group by mr.movie_id
order by sum(mr.rating) / count(*) desc, m.title asc
limit 1
)

# Union by name both (Added union all as union only selects distinct
# values by default)
select results from abc
UNION ALL
select results from def