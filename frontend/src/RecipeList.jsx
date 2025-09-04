function RecipeList({ recipes }) {
  return (
    <div>
      {recipes.map(r => (
        <div key={r.id} style={{border:'1px solid #ccc', margin:'10px', padding:'10px'}}>
          <h3>{r.title}</h3>
          <p><b>Ingredients:</b> {r.ingredients}</p>
          <p><b>Instructions:</b> {r.instructions}</p>
        </div>
      ))}
    </div>
  )
}

export default RecipeList;
