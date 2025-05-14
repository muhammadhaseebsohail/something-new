Here's a basic implementation of the homepage with a display of the latest toys, a navigation menu and a search bar. I'll be using React Hooks, PropTypes, CSS-in-JS and error handling/loading states as requested.

```jsx
import React, { useEffect, useState } from 'react'
import PropTypes from 'prop-types'
import axios from 'axios'
import { makeStyles } from '@material-ui/core/styles'
import { AppBar, Toolbar, Typography, InputBase } from '@material-ui/core'
import SearchIcon from '@material-ui/icons/Search'

// CSS-in-JS
const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  menuButton: {
    marginRight: theme.spacing(2),
  },
  title: {
    flexGrow: 1,
  },
  inputRoot: {
    color: 'inherit',
  },
  inputInput: {
    padding: theme.spacing(1, 1, 1, 0),
    paddingLeft: `calc(1em + ${theme.spacing(4)}px)`,
    transition: theme.transitions.create('width'),
    width: '100%',
    [theme.breakpoints.up('md')]: {
      width: '20ch',
    },
  },
}))

const Home = ({ apiUrl }) => {
  const classes = useStyles()
  const [toys, setToys] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    axios
      .get(apiUrl)
      .then((response) => {
        setToys(response.data)
        setLoading(false)
      })
      .catch((error) => {
        setError(error.message)
        setLoading(false)
      })
  }, [apiUrl])

  if (loading) return <div>Loading...</div>
  if (error) return <div>Error: {error}</div>

  return (
    <div className={classes.root}>
      <AppBar position="static">
        <Toolbar>
          <Typography className={classes.title} variant="h6" noWrap>
            Toy Store
          </Typography>
          <div>
            <SearchIcon />
            <InputBase
              placeholder="Search…"
              classes={{
                root: classes.inputRoot,
                input: classes.inputInput,
              }}
              inputProps={{ 'aria-label': 'search' }}
            />
          </div>
        </Toolbar>
      </AppBar>
      <div>
        {toys.map((toy) => (
          <div key={toy.id}>
            <h2>{toy.name}</h2>
            <img src={toy.image} alt={toy.name} />
            <p>{toy.description}</p>
          </div>
        ))}
      </div>
    </div>
  )
}

Home.propTypes = {
  apiUrl: PropTypes.string.isRequired,
}

export default Home
```

For testing, you can use Jest and Testing Library. Here's a simple test setup for this component.

```jsx
import React from 'react'
import { render } from '@testing-library/react'
import Home from './Home'

test('renders without crashing', () => {
  const { getByText } = render(<Home apiUrl="http://example.com/api/toys" />)
  const linkElement = getByText(/Toy Store/i)
  expect(linkElement).toBeInTheDocument()
})
```

Remember to replace `http://example.com/api/toys` with your real API URL.